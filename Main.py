class T:

    f = ''
    df = ''

    def __init__(self, f, df):
        self.f = f
        self.df = df

    def __add__(self, p):
        p = toT(p)
        return T('(' + self.f + ' + ' + p.f + ')', '(' + self.df + ' + ' + p.df + ')')

    def __sub__(self, p):
        p = toT(p)
        return T('(' + self.f + ' - ' + p.f + ')', '(' + self.df + ' - ' + p.df + ')')

    def __mul__(self, p):
        p = toT(p)
        return T('(' + self.f + ' * ' + p.f + ')', '(' + self.df + ' * ' + p.f + ' + ' + p.df + ' * ' + self.f + ')')

    def __truediv__(self, p):
        p = toT(p)
        return T('(' + self.f + ' / ' + p.f + ')', '((' + self.df + ' * ' + p.f + ' - ' + p.df + ' * ' + self.f + ') / ' + p.f + ' ** 2)')

    def __pow__(self, p):
        p = toT(p)
        return T('(' + self.f + ' ** ' + p.f + ')', '(' + self.f + ' ** ' + p.f + ' * (' + p.df + ' * ln(' + self.f + ') + ' + p.f + ' * ' + self.df + ' / ' + self.f + '))')

    def __radd__(self, p):
        p = toT(p)
        return p + self

    def __rsub__(self, p):
        p = toT(p)
        return p - self

    def __rmul__(self, p):
        p = toT(p)
        return p * self

    def __rtruediv__(self, p):
        p = toT(p)
        return p / self

    def __rpow__(self, p):
        p = toT(p)
        return p ** self

    def __pos__(self):
        return self

    def __neg__(self):
        return T('(-' + self.f + ')', '(-' + self.df + ')')


def toT(p):
    if (type(p) is int) or (type(p) is float):
        return T('(' + str(p) + ')', '0')
    return p


def sin(p):
    p = toT(p)
    return T('sin(' + p.f + ')', '(cos(' + p.f + ') * ' + p.df + ')')


def cos(p):
    p = toT(p)
    return T('cos(' + p.f + ')', '(-sin(' + p.f + ') * ' + p.df + ')')


def ln(p):
    p = toT(p)
    return T('ln(' + p.f + ')', '(' + p.df + ' / ' + p.f + ')')


def tg(p):
    p = toT(p)
    return T('tg(' + p.f + ')', '(' + p.df + ' / cos(' + p.f + ') ** 2)')


def ctg(p):
    p = toT(p)
    return T('ctg(' + p.f + ')', '(-' + p.df + ' / sin(' + p.f + ') ** 2)')


def arcsin(p):
    p = toT(p)
    return T('arcsin(' + p.f + ')', '(' + p.df + ' / (1 - ' + p.f + ' ** 2) ** (1 / 2))')


def arctg(p):
    p = toT(p)
    return T('arctg(' + p.f + ')', '(' + p.df + ' / (1 + ' + p.f + ' ** 2))')

fin = open('deriv.in', 'r')
fout = open('deriv.out', 'w')

lines = fin.readlines()
for i in range(len(lines)):
    sti = lines[i]
    if (sti != '\n'):
        if sti[-1] != '\n': sti = sti + '\n'
        s = sti[:-1] + ' + x - x'
        s = s.replace('e', '2.71828182846')
        x = T('x', '1')
        st = eval(s).df
        fout.write(st + '\n')
        sti = fin.readline()
fin.close()
fout.close()
