from tortoise import Tortoise

TORTOISE_ORM = {
    'connections': {
        'default': 'postgres://ps_user:ps_password@localhost:5432/ps_db'
    },
    'apps': {
        'models': {
            'models': ['models', 'aerich.models'],  # You can define your models here or in separate files
            'default_connection': 'default',
        }
    }
}


async def init():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()
    print("Database connected successfully!")


async def check_db():
    try:
        connection = Tortoise.get_connection("default")
        # Using asyncpg directly for executing the SQL query
        table_names = await connection.execute_query(
            """
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
                AND table_type = 'BASE TABLE'
            ORDER BY table_name;
            """
        )
        print("Database is connected and operational.")
        print("List of table names:")
        for row in table_names[1]:
            print(row)
    except Exception as e:
        print(f"Failed to connect to the database: {e}")


async def close_db():
    await Tortoise.close_connections()
