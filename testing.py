# Function from other project of mine.
def paint(string, rgb, foreground = True, end = True):
    r, g, b = rgb
    return '\x1b' + f'[{38 if foreground else 48};2;{r};{g};{b}m{string}' + ("\x1b[00m" if end else "")
  
def main():
    from time    import sleep      as wait
    from rainbow import rainbowRGB as rRGB

    for n in range(1, 100):
        print(
            paint("| ##### @@@ $ @@@ ##### |", rRGB(n))
        )

        wait(0.02)

if __name__ == '__main__': main()
