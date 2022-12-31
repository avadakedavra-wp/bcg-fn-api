from flask  import request
import src.middleware.connection as connection

payload = list()

def rice_products():
    province = request.args.get('province')
    try:
        if province :
            result = connection.query_database("""SELECT `A_NAME_T` as `อำเภอ` , `P_NAME_T` as `จังหวัด`, `TON_2017` as `ผลผลิตในปี 2017`,
                                                `TON_2018` as `ผลผลิตในปี 2018`,`TON_2019`  as `ผลผลิตในปี 2019`,
                                                `TON_2020`  as `ผลผลิตในปี 2020`,`TON_2021`  as `ผลผลิตในปี 2021`  
                                                from `rice_amphoe` where `P_NAME_T` = '{}'""".format(province))
            for data in result:
                split_data = {
                    "amphoe": data[0],
                    "province": data[1],
                    "total_2017": data[2],
                    "total_2018": data[3],
                    "total_2019": data[4],
                    "total_2020": data[5],
                    "total_2021": data[6]
                }
                payload.append(split_data) 
            return {"result" : payload} , 200 
        else :
            result = connection.query_database("""SELECT `A_NAME_T` as `อำเภอ` , `P_NAME_T` as `จังหวัด`, `TON_2017` as `ผลผลิตในปี 2017`,
                                                `TON_2018` as `ผลผลิตในปี 2018`,`TON_2019`  as `ผลผลิตในปี 2019`,
                                                `TON_2020`  as `ผลผลิตในปี 2020`,`TON_2021`  as `ผลผลิตในปี 2021`  
                                                from `rice_amphoe` LIMIT 50""")
            for data in result:
                split_data = {
                    "amphoe": data[0],
                    "province": data[1],
                    "total_2017": data[2],
                    "total_2018": data[3],
                    "total_2019": data[4],
                    "total_2020": data[5],
                    "total_2021": data[6]
                }
                payload.append(split_data) 
            return {"result" : payload}, 200
    except Exception as e:
        return "Not found!" , 505