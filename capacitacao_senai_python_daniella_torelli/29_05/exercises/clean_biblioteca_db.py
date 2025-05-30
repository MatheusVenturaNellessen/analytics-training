import sqlite3

def remove_test_entries(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Desabilitar FK e iniciar transação
    cursor.execute("PRAGMA foreign_keys = OFF;")
    cursor.execute("BEGIN TRANSACTION;")

    # Percorrer todas as tabelas do usuário
    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
          AND name NOT LIKE 'sqlite_%';
    """)
    tables = [row[0] for row in cursor.fetchall()]

    # Para cada tabela, deletar valores Teste1/2/3 em colunas TEXT
    for tbl in tables:
        cursor.execute(f"PRAGMA table_info({tbl});")
        text_cols = [info[1] for info in cursor.fetchall() if info[2].upper() == 'TEXT']
        for col in text_cols:
            cursor.execute(
                f"DELETE FROM \"{tbl}\" WHERE \"{col}\" IN (?);",
                ('Teste',)
            )

    # Commit, reativar FK e otimizar o banco
    cursor.execute("COMMIT;")
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute("VACUUM;")
    conn.close()

if __name__ == "__main__":
    remove_test_entries('capacitacao_senai_python_daniella_torelli/29_05/exercises/db/biblioteca.db')
