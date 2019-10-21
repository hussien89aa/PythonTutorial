class Poly(object):
    def __init__(self, coeff):
        self.coeff = coeff

    def __str__(self):
        repres = 'P(x)= '
        l = len(self.coeff)
        for idx, c in enumerate(self.coeff):
            if (c > 0):
                repres += f'+{c}X^{l-1-idx}'
            elif(c < 0):
                repres += f'{c}X^{l-1-idx}'
            elif (c == 0):
                pass
        return repres

    def evaluate(self, x0):
        s = 0
        l = len(self.coeff)
        for idx, c in enumerate(self.coeff):
            p = l - 1 - idx
            s += c*x0**p

        return s

    def __call__(self, x0,):
        s = 0
        l = len(self.coeff)
        for idx, c in enumerate(self.coeff):
            p = l - 1 - idx
            s += c*x0**p

        return s

    def __len__(self):
        return len(self.coeff)

    def __getitem__(self, idx):
        return self.coeff[idx]
