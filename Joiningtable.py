import pandas as pd
import sqlite3

database = 'database.sqlite'
conn = sqlite3.connect(database)

tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print(tables)

Joined_Table = pd.read_sql("""
                           SELECT p.Player_Name, t.Team_Name, s.Season_Year
                           FROM player p
                           INNER JOIN team t ON p.Player_Id = t.Team_Id
                            INNER JOIN season s ON p.Player_Id = s.Man_of_the_Series
                            """, conn)
print(Joined_Table)

print("----------------------------------------------------------------")

joined_match = pd.read_sql("""
                          SELECT m.Match_Id, t1.Team_Name AS Team_1, t2.Team_Name AS Team_2
                          FROM Match m
                          INNER JOIN team t1 ON m.Team_1 = t1.Team_Id
                          INNER JOIN team t2 ON m.Team_2 = t2.Team_Id
                          """, conn)
print(joined_match)
print("----------------------------------------------------------------")

union = pd.read_sql("""
        SELECT Match_Id
        FROM Match
        UNION
        SELECT Team_Id
        FROM team    
        """, conn)
print(union)
print("----------------------------------------------------------------")

joined_left = pd.read_sql("""
        SELECT *
        FROM match
        LEFT JOIN season
        ON match.Match_Id = season.Man_of_the_Series
        """, conn)
print(joined_left)
print("----------------------------------------------------------------")

joined_player_season = pd.read_sql_query(""" SELECT m.Match_Id, t.Team_Id
                                    FROM Match m
                                    INNER JOIN team t ON m.Match_Id = t.Team_Id
                                    """, conn)

print(joined_player_season)
print("----------------------------------------------------------------")
