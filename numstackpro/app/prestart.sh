#! /usr/bin/env sh
echo "set -e
exec ~/vsc/code-server --allow-http --no-auth --data-dir /data /code"
echo "Running inside /app/prestart.sh, you could add migrations to this file, e.g.:"

echo "
#! /usr/bin/env bash
# Let the DB start
sleep 10;
# Run migrations
alembic upgrade head
"