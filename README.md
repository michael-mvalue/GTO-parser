# **🧠 PioSolver Metadata Parser**

This Python tool extracts structured metadata from \`.cfr\` output files generated by [PioSolver](https://piosolver.com). It connects directly to the solver via its CLI, pulls tree information and EV metrics, and outputs a JSON-formatted summary suitable for downstream database storage or integration.

---

## **📌 Features**

*   Connects to PioSolver using the \`.exe\` command interface
*   Loads and parses a \`.cfr\` solve file  
*   Extracts core metadata
*   Outputs result as a JSON dictionary

---

## **🧪 Example Use Cases**

*   Extracting GTO solve metadata for machine learning pipelines
*   Populating a searchable database of GTO solve trees
*   Preprocessing for hand comparison or in-game analysis

---

## **🧰 Requirements**

*   python 3.7+
*   PioSolver Pro or Edge installed locally
*   Access to \`.cfr\` solve files (PioSolver output)

---

## **🚀 Usage**

**1\. Set Paths**  
    Edit the following two variables at the top of \`index.py\`:

```python
piosolver_path = r"C:\PioSolver\piosolver.exe"
cfr_file_path = r"C:\PioSolver\projects\sample.cfr"
```

**2\. Run the Parser**

```
python index.py
```

**3\. Sample Output**

```
{
    "config": {
        "flop_bet_size": 33.0,
        "flop_raise_size": 100.0,
        "turn_bet_size": 75.0,
        "river_bet_size": 100.0,
        "flop_ip_bet_size": 100.0,
        "flop_ip_raise_size": 100.0,
        "flop_ip_add_all_in": true,
        "turn_ip_bet_size": 75.0,
        "river_ip_bet_size": 100.0
    },
    "effective_stack": 100.0,
    "ev_oop": 2.114,
    "ev_ip": 3.886,
    "oop_mes": 2.129,
    "ip_mes": 3.894,
    "exploitable": 0.012,
    "board": "As Kd 2c",
    "pot": 6.0,
    "range0": [
        "AA:0.1",
        "KK:0.1",
        "QQ:0.2",
        "JJ:1.0",
        "TT:1.0",
        "99:1.0",
        "88:1.0",
        "77:1.0",
        "66:1.0",
        "55:1.0",
        "44:1.0",
        "33:1.0",
        "22:1.0",
        "AK:0.1",
        "AQs:0.2",
        "AQo:0.4",
        "AJs:0.4",
        "AJo:1.0",
        "ATs:0.9",
        "ATo:1.0",
        "A9s:0.9",
        "A9o:1.0",
        "A8:1.0",
        "A7s:1.0",
        "A6s:1.0",
        "A5s:1.0",
        "A4s:1.0",
        "A3s:1.0",
        "A2s:1.0",
        "KQs:0.9",
        "KQo:1.0",
        "KJs:0.9",
        "KJo:1.0",
        "KTs:0.9",
        "KTo:1.0",
        "K9s:1.0",
        "K8s:1.0",
        "K7s:1.0",
        "K6s:1.0",
        "K5s:1.0",
        "K4s:0.5",
        "K3s:0.5",
        "K2s:0.5",
        "QJs:0.9",
        "QJo:1.0",
        "QTs:0.9",
        "QTo:1.0",
        "Q9s:1.0",
        "Q8s:1.0",
        "Q7s:0.5",
        "Q6s:0.5",
        "JTs:0.9",
        "JTo:1.0",
        "J9s:1.0",
        "J8s:1.0",
        "J7s:0.5",
        "J6s:0.5",
        "T9s:0.5",
        "T8s:1.0",
        "T7s:1.0",
        "T6s:0.5",
        "98s:0.5",
        "97s:0.5",
        "96s:0.5",
        "87s:0.5",
        "86s:0.5",
        "85s:0.3",
        "76s:0.5",
        "75s:0.3",
        "65s:0.5",
        "64s:0.3",
        "54s:0.5",
        "53s:0.3",
        "43s:0.3"
    ],
    "range1": [
        "AA:1.0",
        "KK:1.0",
        "QQ:1.0",
        "JJ:1.0",
        "TT:1.0",
        "99:0.75",
        "88:0.75",
        "77:0.5",
        "66:0.5",
        "55:0.5",
        "44:0.25",
        "AK:1.0",
        "AQ:1.0",
        "AJs:1.0",
        "AJo:0.25",
        "ATs:1.0",
        "A6o:0.25",
        "A5s:0.75",
        "A5o:0.5",
        "A4:0.5",
        "A3:0.5",
        "A2:0.5",
        "KQs:1.0",
        "KQo:0.25",
        "KJs:1.0",
        "KTs:1.0",
        "K6o:0.25",
        "K5o:0.5",
        "K4o:0.5",
        "K3o:0.5",
        "K2o:0.5",
        "QJs:1.0",
        "QTs:0.5",
        "Q5o:0.25",
        "Q4o:0.25",
        "Q3o:0.25",
        "Q2o:0.25",
        "JTs:0.75",
        "J9s:0.25",
        "J4o:0.25",
        "J3o:0.25",
        "T9s:0.75",
        "T8s:0.25",
        "98s:0.75",
        "98o:0.25",
        "97s:0.25",
        "87s:0.75",
        "87o:0.25",
        "86s:0.25",
        "76s:0.75",
        "76o:0.25",
        "75s:0.25",
        "65s:0.75",
        "65o:0.25",
        "64s:0.25",
        "54s:0.75",
        "54o:0.25"
    ],
    "solve_id": "0b9b85692b4b822c0fe881f7aee6a5006a642a8f"
}
```

---

## **🧪 run your test:**

```bash
python -m unittest test/parser_test.py
```
---