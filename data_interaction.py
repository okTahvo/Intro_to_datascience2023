import pandas as pd
import plotly.express as px

def draw_radar_graph(data):
    a = data["processor clock speed to price"].mean()
    b = data["drive capacity to price"].mean()
    c = data["RAM to price"].mean()
    d = data["GPU memory to price"].mean()
    e = data["pixel count to price"].mean()
    f = data["screen size to price"].mean()
    g = data["weight to price"].mean()
    #print({'clock speed score':a, 'drive capacity score':b, 'RAM score':c, 'GPU memory score':d, 'pixel count score':e, 'screen size score':f, 'weight score':g})
    dataf = pd.DataFrame(dict(r=[a, b, c, d, e, f, g], theta=['clock speed', 'drive capacity', 'RAM', 'GPU memory', 'pixel count', 'screen size', 'weight']))
    fig = px.line_polar(dataf, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself')
    fig.show()

def filter_data(data):
    for fiel in ["brand", "processor brand"]:
        values = sorted(data[fiel].unique())
        print(values)
        an = input("Please write one of the items in the list above. Any other answer skips: ")
        if an in values:
            data = data[data[fiel]==an]
    for field in ["webcam", "microphone", "touchscreen", "speakers", "SSD"]:
        message = "Would you like to have "+field+"?"
        print(message)
        ans = input("Yes/No. Any other answer skips: ")
        if ans == "Yes":
            data = data[data[field]==True]
        elif ans == "No":
            data = data[data[field]==False]
    if data.shape[0] == 0:
        return (data, False)
    return (data, True)

def add_entry():
    entry = {}
    entry["brand"] = input("Please enter laptop brand: ")
    entry["price"] = int(input("Please enter price in Indian rupees: "))
    entry["processor brand"] = input("Please enter processor brand: ")
    entry["processor number"] = int(input("Please enter processor number (e.g. Intel i9 = 9): "))
    entry["processor year"] = int(input("Please enter processor year: "))
    entry["processor clock speed"] = float(input("Please enter maximum processor clock speed (GHz): "))
    entry["processor core count"] = int(input("Please enter number of processor cores: "))
    a = input("Does the laptop have SSD? Any answer other than 'Yes' will be interpreted as 'No'. Answer: ")
    if a == "Yes":
        entry["SSD"] = True
    else:
        entry["SSD"] = False
    entry["drive capacity"] = int(input("Please enter drive capacity (GB): "))
    entry["RAM"] = int(input("Please enter RAM capacity (GB): "))
    entry["GPU memory"] = int(input("Please enter dedicated GPU capacity (GB): "))
    entry["screen size"] = input("Please enter screen size in inches: ")
    entry["pixel count"] = int(input("Please enter total number of pixels: "))
    entry["weight"] = input("Please enter weight (kg): ")
    for item in ["speakers", "touchscreen", "microphone", "webcam"]:
        mes = "Does the laptop have "+item+"? Any answer other than 'Yes' will be interpreted as 'No'. Answer: "
        a = input(mes)
        if a == "Yes":
            entry[item] = True
        else:
            entry[item] = False
    return entry

def convert_to_float(value):
    try:
        return float(value)
    except:
        return None

if __name__ == '__main__':
    df = pd.read_csv("preprocessed_laptop_data.csv")#read data
    df["screen size"] = df["screen size"].apply(convert_to_float)
    df["weight"] = df["weight"].apply(convert_to_float)
    for field in ["processor clock speed", "drive capacity", "RAM", "GPU memory", "pixel count", "screen size", "weight"]:#compute scores for features
        df[field] = df[field].fillna(df[field].mean())
        name = field+" to price"
        df[name] = (df[field])/(df["price"])
        maxi = df[name].max()
        df[name] = (df[name])/maxi
    df2 = df.copy()
    print("Hello! I am an interaction tool for the data.")
    while True:
        print("What would you like me to do?")
        print("1: Draw radar chart")
        print("2: Filter data")
        print("3: Add a new entry")
        print("q: quit")
        answer = input("answer: ")
        if answer == "1":#draw radar graph
            draw_radar_graph(df2)
        elif answer == "2":#filter data
            df2 = df.copy()
            success = filter_data(df2)
            if success[1] == False:
                print("No matching data")
            else:
                df2 = success[0]
        elif answer == "3":#create a new entry (not written to any dataframes or databases)
            entry = add_entry()
            print(entry)
        elif answer == "q":#exit
            print("Have a nice day!")
            break
