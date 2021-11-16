from optcap import OptCap, Color


def create_as():
    a1 = OptCap(Color.w, inst_id="a1", x="A")
    a2 = OptCap(Color.w, inst_id="a2", x="C")
    a3 = OptCap(Color.w, inst_id="a3", x="D")
    a4 = OptCap(Color.w, inst_id="a4", x="D")
    a5 = OptCap(Color.w, inst_id="a5", x="D")
    a6 = OptCap(Color.w, inst_id="a5", x="E")
    return [a1, a2, a3, a4, a5, a6]


def create_bs():
    b1 = OptCap(Color.b, inst_id="b1", x="C")
    b2 = OptCap(Color.b, inst_id="b2", x="B")
    b3 = OptCap(Color.b, inst_id="b3", x="C")
    b4 = OptCap(Color.b, inst_id="b4", x="D")
    b5 = OptCap(Color.b, inst_id="b5", x="E")
    return [b1, b2, b3, b4, b5]
