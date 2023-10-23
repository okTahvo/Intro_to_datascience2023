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

if __name__ == '__main__':
    df = pd.read_csv("preprocessed_laptop_data.csv")
    for field in ["processor clock speed", "drive capacity", "RAM", "GPU memory", "pixel count"]:
        name = field+" to price"
        df[name] = (df[field])/(df["price"])
        maxi = df[name].max()
        df[name] = (df[name])/maxi
    print(df.head())
    print("Hello! I am an interaction tool for the data.")
    while True:
        print("What would you like me to do?")
        print("1: Draw radar chart")
        print("2: Filter data")
        print("q: quit")
        answer = input("answer: ")
        if answer == "1":
            draw_radar_graph(df)
        elif answer == "2":
            pass
        elif answer == "q":
            print("Have a nice day!")
            break
