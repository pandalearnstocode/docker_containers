from fastapi import FastAPI
import coloredlogs, logging
coloredlogs.install(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", isatty=True,milliseconds=True)
app = FastAPI()
logger = logging.getLogger("app")

@app.get("/")
def read_root():
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is a error message.")
    return {"Hello": "World"}