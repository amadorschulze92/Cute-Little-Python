### RANDO SCRIPT THAT COVERS ALL THESE TOPICS
# 1) Convert int, float, str, list, and dict data types
# 2) Conditional statements + nesting
# 3) For and while loops
# 4) selecting values in list or string
# 5) add or remove elements from dict or list
# 6) print, range, round, len, min, max, split
# 7) read and write different kinds of files
# 8) Installing, importing, and using packages

import pandas as pd

def half_len(my_list):
    half_list = []
    for i in my_list:
        i_len = len(i)
        half1 = i[:int(i_len/2)]
        half2 = i[int(i_len/2):]
        print(half1)
        half_list.append([str(half1),str(half2)])
    return half_list

def is_sound(my_list):
    for x in my_list:
        if x[0] == x[1]:
            print("{0} {1}".format(x[0], "True"))
        else:
            print("{0} {1}".format(x[0], "False"))


def main():
    df = pd.read_csv("usf_prep_dummy_data.csv")
    df = df.astype({"Cost ($)": float, "stock": str})

    sound_list = list(df["sound"])
    half_list = half_len(sound_list)

    is_sound(half_list)

    print(df.head())

    print("df length: " + str(len(df)))
    print("max cost: " + str(max(df["Cost ($)"])))
    print("min cost: " + str(min(df["Cost ($)"])))

    print("\nfinished...")

if __name__ == '__main__':
    import plac
    plac.call(main)
