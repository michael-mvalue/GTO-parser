from solver import Solver
import json
import hashlib
import os
from validation.utility import (
    validate_metadata,
    safe_extract,
    safe_float,
    cast_bool
)

piosolver_path = r"C:\PioSolver\piosolver.exe"
cfr_file_path = r"C:\PioSolver\projects\sample.cfr"

def extract_metadata():
    if not os.path.exists(piosolver_path):
        raise FileNotFoundError("PioSolver path is invalid.")
    if not os.path.exists(cfr_file_path):
        raise FileNotFoundError("CFR file path is invalid.")
    
    data = {}
    data['config'] = {}
    # starts the solver process using the provided .exe path
    connection = Solver(solver=piosolver_path)
    connection.command(line=f"load_tree {cfr_file_path}")
    [effective_stack] = connection.command("show_effective_stack")
    data['effective_stack'] = float(effective_stack)

    [EV_OOP, EV_IP, OOP_MES, IP_MES, Exploitable] = connection.command("calc_results")
    data['ev_oop'] = safe_float(r'EV OOP: ([\d\.]+)', EV_OOP)
    data['ev_ip'] = safe_float(r'EV IP: ([\d\.]+)', EV_IP)
    data['oop_mes'] = safe_float(r"OOP's MES: ([\d\.]+)", OOP_MES)
    data['ip_mes'] = safe_float(r"IP's MES: ([\d\.]+)", IP_MES)
    data['exploitable'] = safe_float(r'Exploitable for: ([\d\.]+)', Exploitable)

    tree_info = connection.command("show_tree_info")
    data['board'] = safe_extract(r'#Board#([\w\s]+)', tree_info[3])
    data['pot'] = safe_extract(r'#Pot#([\d\.]+)', tree_info[4], float)
    data['config']['flop_bet_size'] = safe_extract(r'#FlopConfig.BetSize#([\d\.]+)', tree_info[8], float)
    data['config']['flop_raise_size'] = safe_extract(r'#FlopConfig.RaiseSize#([\d\.]+)', tree_info[9], float)
    data['config']['turn_bet_size'] = safe_extract(r'#TurnConfig.BetSize#([\d\.]+)', tree_info[10], float)
    data['config']['river_bet_size'] = safe_extract(r'#RiverConfig.BetSize#([\d\.]+)', tree_info[11], float)
    data['config']['flop_ip_bet_size'] = safe_extract(r'#FlopConfigIP.BetSize#([\d\.]+)', tree_info[12], float)
    data['config']['flop_ip_raise_size'] = safe_extract(r'#FlopConfigIP.RaiseSize#([\d\.]+)', tree_info[13], float)
    data['config']['flop_ip_add_all_in'] = safe_extract(r'#FlopConfigIP\.AddAllin#([^#]+)', tree_info[14], cast_type=cast_bool)
    data['config']['turn_ip_bet_size'] = safe_extract(r'#TurnConfigIP.BetSize#([\d\.]+)', tree_info[15], float)
    data['config']['river_ip_bet_size'] = safe_extract(r'#RiverConfigIP.BetSize#([\d\.]+)', tree_info[16], float)
    data['range0'] = [h if ':' in h else f"{h}:1.0" for h in tree_info[1].split("#Range0#")[-1].split(",")]
    data['range1'] = [h if ':' in h else f"{h}:1.0" for h in tree_info[2].split("#Range1#")[-1].split(",")]
    # rangeOOP = connection.command("show_range OOP r")
    # rangeIP = connection.command("show_range IP r")
    # evOOP = connection.command("calc_ev OOP r:0")
    # evIP = connection.command("calc_ev IP r:0")
    
    solve_id_source = f"{data.get('board', '')}{data.get('effective_stack', '')}{data.get('ev_oop', '')}{data.get('ev_ip', '')}"
    data["solve_id"] = hashlib.sha1(solve_id_source.encode()).hexdigest()
        
    validate_metadata(data)

    print("Closing connection...")
    connection.exit()
    print("Solver Connection closed!")
    return data

if __name__ == "__main__":
    res = extract_metadata()
    print(json.dumps(res, indent=4))