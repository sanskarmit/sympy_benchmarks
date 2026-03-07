from sympy import cos, expand_trig, sin, symbols, trigsimp


class TimeTrigSimplify:
    """Benchmark trigonometric simplification on expanded angle-sum identities."""

    params = [5, 10, 20]

    def setup(self, n):
        xs = symbols(f"x0:{n + 1}")
        expr = 0
        for i in range(n):
            angle = xs[i] + xs[i + 1]
            # Keep a non-trivial expanded form that should simplify back to 1.
            expr += expand_trig(sin(angle) ** 2 + cos(angle) ** 2)
        self.expr = expr

    def time_trigsimp(self, n):
        trigsimp(self.expr)
