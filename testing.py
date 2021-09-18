# Function from other project of mine.
def paint(string, rgb, foreground = True, end = True):
    r, g, b = rgb
    return '\x1b' + f'[{38 if foreground else 48};2;{r};{g};{b}m{string}' + ("\x1b[00m" if end else "")
  
def rprint(string):
    from rainbow import rainbowRGB as rRGB
    
    # Loops throught each letter and applies an color.
    for n in range(len(string)):
        print(
            paint(string[n], rRGB(n + 1)), end = ""
        )

def main():
    rprint("#### Yeah, this seems nice. #####")

if __name__ == '__main__': main()
