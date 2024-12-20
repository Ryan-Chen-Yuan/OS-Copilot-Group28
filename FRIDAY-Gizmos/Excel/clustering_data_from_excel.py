import pandas as pd
from sklearn.cluster import KMeans
from openpyxl import load_workbook

def clustering_data_from_excel(excel_path, sheet_name, column_name):
    """
    从Excel文件中读取某一列数据,使用k-means算法进行聚类分析,并将该列数据属于哪一类输出到新的一列中。

    Args:
    excel_path (str): Excel文件的路径。
    sheet_name (str): 工作表的名称。
    column_name (str): 需要聚类的列名。

    Returns:
    None
    """
    # 读取Excel文件中的数据
    df = pd.read_excel(excel_path, sheet_name=sheet_name)

    # 提取需要聚类的列
    data_to_cluster = df[[column_name]]

    # 使用k-means算法进行聚类
    kmeans = KMeans(n_clusters=4, random_state=0)
    df['Cluster'] = kmeans.fit_predict(data_to_cluster)

    # 将结果写回到Excel文件中
    with pd.ExcelWriter(excel_path, engine='openpyxl', mode='a') as writer:
        writer.book = load_workbook(excel_path)
        writer.sheets = {ws.title: ws for ws in writer.book.worksheets}
        df.to_excel(writer, sheet_name=sheet_name, index=False)

    print("Excel文件已更新,新增一列标出聚类结果。")

# 示例调用
# clustering_data_from_excel('data.xlsx', 'Sheet1', 'Column1')