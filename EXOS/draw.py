def dessine(root, val="val", gauche="gauche", droit="droit"):
    def display(root, val=val, gauche=gauche, droit=droit):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, droit) is None and getattr(root, gauche) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only gauche child.
        if getattr(root, droit) is None:
            lines, n, p, x = display(getattr(root, gauche))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only droit child.
        if getattr(root, gauche) is None:
            lines, n, p, x = display(getattr(root, droit))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        gauche, n, p, x = display(getattr(root, gauche))
        droit, m, q, y = display(getattr(root, droit))
        s = '%s' % getattr(root, val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            gauche += [n * ' '] * (q - p)
        elif q < p:
            droit += [m * ' '] * (p - q)
        zipped_lines = zip(gauche, droit)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, val, gauche, droit)
    for line in lines:
        print(line)
