


class MostUsedOpcodes(object):
    def __init__(self, fil):
        self.fil = fil
        self._seqs = []

    def read(self):
        self._seqs = []
        with open(self.fil, 'r') as inp:
            for seq in inp.readlines():
                self._seqs.append([int(opcode) for opcode in seq.split(",")])
        

    def write(self):
        with open(self.fil, 'w') as out:
            for seq in self._seqs:
                for i in range(len(seq)):
                    out.write(str(seq[i]))
                    if i < len(seq) - 1:
                        out.write(',')
                out.write('\n')

    @property
    def seqs(self):
        self.read()
        return self._seqs

    @seqs.setter
    def seqs(self, val):
        self._seqs = val
        self.write()
