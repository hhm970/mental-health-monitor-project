source .env
export PGPASSWORD=$DB_PASSWORD


createdb --host $DB_HOST -p $DB_PORT -U $DB_USER $DB_NAME