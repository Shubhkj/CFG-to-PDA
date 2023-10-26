import tkinter as tk

def convert_cfg_to_pda():
    cfg_rules = input_text.get("1.0", "end-1c").split('\n')
    pda_rules = []

    for rule in cfg_rules:
        if rule:
            left, right = rule.split('->')
            left = left.strip()
            right = right.strip()

            if right == 'null':
                pda_rules.append(f"dl(q,0,0) --> dl(q,{left})")
            else:
                for symbol in right.split('|'):
                    pda_rules.append(f"dl(q,null,{left}) --> dl(q,{symbol})")

    output_text.delete("1.0", "end")
    output_text.insert("1.0", '\n'.join(pda_rules))

root = tk.Tk()
root.title("CFG to PDA Converter")

input_label = tk.Label(root, text="Enter CFG Rules:")
input_label.pack()

input_text = tk.Text(root, height=5, width=30)
input_text.pack()

convert_button = tk.Button(root, text="Convert", command=convert_cfg_to_pda)
convert_button.pack()

output_label = tk.Label(root, text="PDA Rules:")
output_label.pack()

output_text = tk.Text(root, height=5, width=30)
output_text.pack()

root.mainloop()
