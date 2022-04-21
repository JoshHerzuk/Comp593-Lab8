from tkinter import *
from tkinter import ttk
from pokeAPI import get_poke_info


def main():

#create the window
    root = Tk()
    root.title("Pokemon Info Viewer")
    root.iconbitmap('pokeball.ico')
    root.resizable(False, False)

#create the frames
    frm_input = ttk.Frame(root)
    frm_input.grid(row=1, column=1, columnspan=2)

    frm_stats = ttk.LabelFrame(root, text="Stats")
    frm_stats.grid(row=2, column=2, padx=10, pady=10, sticky=N)

    frm_info = ttk.LabelFrame(root, text="Info")
    frm_info.grid(row=2, column=1, padx=10, pady=10, sticky=N)

#populate user input frame
    lbl_name = ttk.Label(frm_input, text="Pokemon Name:")
    lbl_name.grid(row=1, column=1, padx=10, pady=10)

    ent_name = ttk.Entry(frm_input)
    ent_name.grid(row=1, column=2)

    def btn_get_info_click():
        name = ent_name.get()
        poke_dict = get_poke_info(name)
        if poke_dict:
            lbl_height_val['text'] = str(poke_dict['height']) + ' dm'
            lbl_weight_val['text'] = str(poke_dict['weight']) + ' lbs' 
            types_list = [t['type']['name']for t in poke_dict['types']]
            lbl_type_val['text'] = ', '.join(types_list)
            prg_hp['value'] = poke_dict['stats'][0]['base_stat']
            prg_atk['value'] = poke_dict['stats'][1]['base_stat']
            prg_def['value'] = poke_dict['stats'][2]['base_stat']
            prg_sp_atk['value'] = poke_dict['stats'][3]['base_stat']
            prg_sp_def['value'] = poke_dict['stats'][4]['base_stat']
            prg_speed['value'] = poke_dict['stats'][5]['base_stat']


    btn_get_info = ttk.Button(frm_input, text='Get Info', command=btn_get_info_click)
    btn_get_info.grid(row=1, column=3, padx=10, pady=10)

#populate the stats frame

    lbl_hp = ttk.Label(frm_stats, text='HP:')
    lbl_hp.grid(row=1, column=1, padx=10, pady=10, sticky=E)
    prg_hp = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_hp.grid(row=1, column=2, padx=10)

    lbl_atk = ttk.Label(frm_stats, text='Attack:')
    lbl_atk.grid(row=2, column=1, padx=10, pady=10, sticky=E)
    prg_atk = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_atk.grid(row=2, column=2, padx=10)

    lbl_def = ttk.Label(frm_stats, text='Defense:')
    lbl_def.grid(row=3, column=1, padx=10, pady=10, sticky=E)
    prg_def = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_def.grid(row=3, column=2, padx=10)

    lbl_sp_atk = ttk.Label(frm_stats, text='Special Attack:')
    lbl_sp_atk.grid(row=4, column=1, padx=10, pady=10, sticky=E)
    prg_sp_atk = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_sp_atk.grid(row=4, column=2, padx=10)

    lbl_sp_def = ttk.Label(frm_stats, text='Special Defense:')
    lbl_sp_def.grid(row=5, column=1, padx=10, pady=10, sticky=E)
    prg_sp_def = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_sp_def.grid(row=5, column=2, padx=10)

    lbl_speed = ttk.Label(frm_stats, text='Speed:')
    lbl_speed.grid(row=6, column=1, padx=10, pady=10, sticky=E)
    prg_speed = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_speed.grid(row=6, column=2, padx=10)

#populate pokemon info frame
    lbl_height = ttk.Label(frm_info, text="Height:")
    lbl_height.grid(row=1, column=1, padx=10, pady=10, stick=E)
    lbl_height_val = ttk.Label(frm_info, text='...', width=15)
    lbl_height_val.grid(row=1, column=2)

    lbl_weight = ttk.Label(frm_info, text='Weight:')
    lbl_weight.grid(row=2, column=1, padx=10, pady=10, stick=E)
    lbl_weight_val = ttk.Label(frm_info, text="...", width=15)
    lbl_weight_val.grid(row=2, column=2)

    lbl_type = ttk.Label(frm_info, text='Type:')
    lbl_type.grid(row=3, column=1, padx=10, pady=10, stick=E)
    lbl_type_val = ttk.Label(frm_info, text="...", width=15)
    lbl_type_val.grid(row=3, column=2)
    

    root.mainloop()   





main()