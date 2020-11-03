
from astroboi_bio_tools.ToolLogic import ToolLogics
class Logics(ToolLogics):
    def get_idx_list_frm_long_seq_by_input_seq(self, long_seq, input_seq):
        idx_list = []
        len_input = len(input_seq)
        for i in range(len(long_seq) - len_input):
            if self.match(0, long_seq[i: i + len_input], input_seq):
                idx_list.append(i)
        return idx_list

    def append_flag_by_freq(self, data_list, append_trgt):
        frequency = len(data_list)
        if frequency == 1:
            append_trgt.append('True')
        elif frequency > 1:
            append_trgt.append('False')
        else:
            append_trgt.append('')