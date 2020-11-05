txtfile = "t.txt"
# read the text file

def read_text_file():
    with open (txtfile, "r") as f:
        t = f.readlines()
        return(t)

def parse_text():
    z = (read_text_file())
    z = "".join(z)
    z = z.split()

    dc = {}
    for i in z:
        if i in dc:
            dc[i] += 1
        else:
            dc[i] = 1
    print(dc)        

    for k,v in dc.items():
        if v == 1:
            print(f"Word occurring once = {k}")

# main driver
if __name__ == "__main__":
    parse_text()