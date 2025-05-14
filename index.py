from solver import Solver
import json
import re
import hashlib

piosolver_path = r"C:\PioSolver\piosolver.exe"
cfr_file_path = r"C:\PioSolver\projects\sample.cfr"

def extract_metadata():
    data = {}
    data['config'] = {}
    # starts the solver process using the provided .exe path
    connection = Solver(solver=piosolver_path)
    print("Solver Connected!")

    connection.command(line=f"load_tree {cfr_file_path}")
    [effective_stack] = connection.command("show_effective_stack")
    # rangeOOP = connection.command("show_range OOP r")
    # rangeIP = connection.command("show_range IP r")
    # evOOP = connection.command("calc_ev OOP r:0")
    # evIP = connection.command("calc_ev IP r:0")

    data['effective_stack'] = float(effective_stack)

    # get EV OOP, EV IP, OOP"s <ES, IP's MES, exploitable for 
    [EV_OOP, EV_IP, OOP_MES, IP_MES, Exploitable] = connection.command("calc_results")
    ev_oop_match = re.search(r'EV OOP: ([\d\.]+)', EV_OOP)
    ev_ip_match = re.search(r'EV IP: ([\d\.]+)', EV_IP)
    oop_mes_match = re.search(r"OOP's MES: ([\d\.]+)", OOP_MES)
    ip_mes_match = re.search(r"IP's MES: ([\d\.]+)", IP_MES)
    exploitable_match = re.search(r'Exploitable for: ([\d\.]+)', Exploitable)
    
    if ev_oop_match:
        data['ev_oop'] = float(ev_oop_match.group(1))
    if ev_ip_match:
        data['ev_ip'] = float(ev_ip_match.group(1))
    if oop_mes_match:
        data['oop_mes'] = float(oop_mes_match.group(1))
    if ip_mes_match:
        data['ip_mes'] = float(ip_mes_match.group(1))
    if exploitable_match:
        data['exploitable'] = float(exploitable_match.group(1))

    # get the tree  info: Board, Pot, EffefctiveStack, AllinThreshold, ...
    tree_info = connection.command("show_tree_info")

    range0 = [hand if ':' in hand else f"{hand}:1.0" for hand in tree_info[1].split("#Range0#")[-1].split(",")]
    range1 = [hand if ':' in hand else f"{hand}:1.0" for hand in tree_info[2].split("#Range1#")[-1].split(",")]
    board_match = re.search(r'#Board#([\w\s]+)', tree_info[3])
    pot_match = re.search(r'#Pot#([\d\.]+)', tree_info[4])
    config1 = re.search(r'#FlopConfig.BetSize#([\d\.]+)', tree_info[8])
    config2 = re.search(r'#FlopConfig.RaiseSize#([\d\.]+)', tree_info[9])
    config3 = re.search(r'#TurnConfig.BetSize#([\d\.]+)', tree_info[10])
    config4 = re.search(r'#RiverConfig.BetSize#([\d\.]+)', tree_info[11])
    config5 = re.search(r'#FlopConfigIP.BetSize#([\d\.]+)', tree_info[12])
    config6 = re.search(r'#FlopConfigIP.RaiseSize#([\d\.]+)', tree_info[13])
    config7 = re.search(r'#FlopConfigIP\.AddAllin#([^#]+)', tree_info[14])
    config8 = re.search(r'#TurnConfigIP.BetSize#([\d\.]+)', tree_info[15])
    config9 = re.search(r'#RiverConfigIP.BetSize#([\d\.]+)', tree_info[16])

    # Extract board
    if board_match:
        data['board'] = board_match.group(1).strip()
    
    # Extract Pot
    if pot_match:
        data['pot'] = float(pot_match.group(1))

    # Extract Range
    if range0:
        data['range0'] = range0

    if range1:
        data['range1'] = range1

    # Extract Config
    if config1:
        data['config']['flop_bet_size'] = float(config1.group(1))

    if config2:
        data['config']['flop_raise_size'] = float(config2.group(1))
    
    if config3:
        data['config']['turn_bet_size'] = float(config3.group(1))
    
    if config4:
        data['config']['river_bet_size'] = float(config4.group(1))
    
    if config5:
        data['config']['flop_ip_bet_size'] = float(config4.group(1))
    
    if config6:
        data['config']['flop_ip_raise_size'] = float(config6.group(1))
    
    if config7:
        data['config']['flop_ip_add_all_in'] = bool(config7.group(1).strip())
    
    if config8:
        data['config']['turn_ip_bet_size'] = float(config8.group(1))

    if config9:
        data['config']['river_ip_bet_size'] = float(config9.group(1))

    solve_id_source = f"{data.get('board', '')}{data.get('effective_stack', '')}{data.get('ev_oop', '')}{data.get('ev_ip', '')}"
    data["solve_id"] = hashlib.sha1(solve_id_source.encode()).hexdigest()
        
    print("Closing connection...")
    connection.exit()
    print("Solver Connection closed!")
    return data

if __name__ == "__main__":
    res = extract_metadata()
    print(json.dumps(res, indent=4))