import time
import os
from Bio import SeqIO
import multiprocessing as mp
import numpy as np
import platform

import Util
import Logic
# import LogicPrep
############### start to set env ################
WORK_DIR = os.getcwd() + "/"
PROJECT_NAME = WORK_DIR.split("/")[-2]
SYSTEM_NM = platform.system()

if SYSTEM_NM == 'Linux':
    # REAL
    pass
else:
    # DEV
    WORK_DIR = "D:/000_WORK/JangHyeWon/20201030/WORK_DIR/"

VEGFA_pegRNA = "VEGFA_pegRNA.txt"
GAGACG_multiple = "GAGACG"
CGTCTC_multiple = "CGTCTC"


TOTAL_CPU = mp.cpu_count()
MULTI_CNT = int(TOTAL_CPU*0.8)
############### end setting env #################

def test():
    util = Util.Utils()
    logic = Logic.Logics()
    rna_list = util.read_tsv_ignore_N_line(WORK_DIR + '/input/' + VEGFA_pegRNA, 2)

    for tmp_rna in rna_list:
        tot_seq = tmp_rna[-2].upper()
        GAGACG_list = logic.get_idx_list_frm_long_seq_by_input_seq(tot_seq, GAGACG_multiple)
        logic.append_flag_by_freq(GAGACG_list, tmp_rna)
        CGTCTC_list = logic.get_idx_list_frm_long_seq_by_input_seq(tot_seq, CGTCTC_multiple)
        logic.append_flag_by_freq(CGTCTC_list, tmp_rna)

    header = 'pegRNA group	spacer sequence	spacer GC content	PAM	strand	peg-to-edit distance	pegRNA extension	extension first base	PBS length	PBS GC content	PBS Tm	RTT length	RTT GC content	INDEX	Barcode-cover	U6 (FP binding)	N19 (gRNA)	BsmBI site 1	"Barcode(MID, 12nt)"	"BsmBI site 2"	RT-PBS	Poly T	Barcode for sorting(12nt)	RP Binding site	Total seq	Total len	GAGACG_multiple	CGTCTC_multiple'.split('\t')
    # header = []
    util.make_excel(WORK_DIR + "/output/VEGFA_pegRNA lib_bsmbi removal", header, rna_list)



if __name__ == '__main__':
    start_time = time.perf_counter()
    print("start [ " + PROJECT_NAME + " ]>>>>>>>>>>>>>>>>>>")
    test()
    print("::::::::::: %.2f seconds ::::::::::::::" % (time.perf_counter() - start_time))

"""
pegRNA group	spacer sequence	spacer GC content	PAM	strand	peg-to-edit distance	pegRNA extension	extension first base	PBS length	PBS GC content	PBS Tm	RTT length	RTT GC content	INDEX	Barcode-cover	U6 (FP binding)	N19 (gRNA)	BsmBI site 1	"Barcode(MID, 12nt)"	"BsmBI site 2"	RT-PBS	Poly T	Barcode for sorting(12nt)	RP Binding site	Total seq	Total len	GAGACG_multiple	CGTCTC_multiple
"""
