import pandas as pd
import plotly.express as px

def draw_radar_graph(data):
    a = data["processor clock speed to price"].mean()
    b = data["drive capacity to price"].mean()
    c = data["RAM to price"].mean()
    d = data["GPU memory to price"].mean()
    e = data["pixel count to price"].mean()
    print({'clock speed':a, 'drive capacity':b, 'RAM':c, 'GPU memory':d, 'pixel count':e})
    dataf = pd.DataFrame(dict(r=[a, b, c, d, e], theta=['clock speed', 'drive capacity', 'RAM', 'GPU memory', 'pixel count']))
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

if __name__ == '__main__':
    df = pd.read_csv("preprocessed_laptop_data.csv")
    for field in ["processor clock speed", "drive capacity", "RAM", "GPU memory", "pixel count"]:
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
        print("q: quit")
        answer = input("answer: ")
        if answer == "1":
            draw_radar_graph(df2)
        elif answer == "2":
            df2 = df.copy()
            success = filter_data(df2)
            if success[1] == False:
                print("No matching data")
            else:
                df2 = success[0]
        elif answer == "q":
            print("Have a nice day!")
            break
