import pandas as pd
#从股票价格到收益率：第一份金融时间序列分析
#把股票价格数据转换成可以用于分析的收益率数据

#模拟8个交易日的股票收盘价
prices=[100,102,101,104,103,106,105,108]

#生成8个工作日日期
dates=pd.bdate_range(start='2026-01-05',periods=8)

#构建DataFrame
df=pd.DataFrame({"Close":prices},index=dates)

df.index.name="Date"
print(df)

#step 2：计算每日收益率并且删除缺失值
df["Daily_Return"]=df["Close"].pct_change()
df=df.dropna(subset=["Daily_Return"])
print(df)

#step 3：（在只已知每日收益率的情况下）计算累计收益率
df["Cumulative_Return"]=(
    (1+df["Daily_Return"]).cumprod()-1
)
print(df)

#step 4：验证结果
import math

#使用首尾价格计算总收益
expected_return=prices[-1]/prices[0]-1

#使用每日收益率复利计算
calculated_return=df["Cumulative_Return"].iloc[-1]

#验证两种方法结果一致
assert math.isclose(
    calculated_return,
    expected_return,
    rel_tol=1e-10
)

print(f"累计收益率：{calculated_return:.2%}")
print("验证通过！")
df.to_csv("stock_returns.csv")