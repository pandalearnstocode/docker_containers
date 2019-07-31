from fastapi import FastAPI
from BLAS_simulation import *
import time
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/simulation_size/{n}")
async def api_intel_RG(n: int):
    base_RG(n)
    start = time.time()
    base_RG(n)
    end = time.time()
    return {"function_name":"api_intel_RG","n": n, "execusion_time":end - start}

@app.get("/base_rand_int_1d/{n}")
async def api_base_rand_int_1d(n: int):
    base_rand_int_1d(min_value=0,max_value=100,sample_size=n)
    start = time.time()
    base_rand_int_1d(min_value=0,max_value=100,sample_size=n)
    end = time.time()
    return {"function_name":"api_base_rand_int_1d","n": n,"execusion_time":end - start}

@app.get("/base_rand_int_2d/{n}")
async def api_base_rand_int_2d(n: int):
    base_rand_int_2d(min_value=0,max_value=100,sample_size=n)
    start = time.time()
    base_rand_int_2d(min_value=0,max_value=100,sample_size=n)
    end = time.time()
    return {"function_name":"base_rand_int_2d","n": n,"execusion_time":end - start}