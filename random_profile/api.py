import sys
import uvicorn
from fastapi import FastAPI, Depends
from fastapi.openapi.utils import get_openapi
from pydantic import create_model

sys.path.append('.')
from random_profile.main import RandomProfile, VERSION

# random_profile==0.2.3 required
rp = RandomProfile()
app = FastAPI()

query_limit = 1000
query_model = create_model("num", num=(int, ...))

metadata = {
    "status": "200",
    "message": "Success",
    "version": VERSION,
    "author": "Deepak Raj",
    "author_email": "deepak008@live.com",
    "github": "https://github.com/codeperfectplus"}

overloaded_error = {"status": "429",
                    "Error": "Too Many Requests",
                    "message": "Number of profiles should be less than {}".format(query_limit)}


@app.get("/")
def index():
    return metadata


@app.get('/api/v1/random_profile/full_profile')
async def get_full_profile(params: query_model = Depends()):
    """ Get multiple profile with all details

    args:
        num (int): number of profiles to generate
    """
    params_as_dict = params.dict()
    if params_as_dict['num'] > query_limit:
        return overloaded_error

    num = params_as_dict['num']
    profile = rp.full_profile(num)
    metadata['data'] = profile
    return metadata


@app.get('/api/v1/random_profile/first_name')
async def get_first_name(params: query_model = Depends()):
    """ Get multiple first names

    args:
        num (int): number of first names to generate

    """
    params_as_dict = params.dict()
    if params_as_dict['num'] > query_limit:
        return overloaded_error

    num = params_as_dict['num']
    first_names = rp.first_name(num)
    metadata['data'] = first_names
    return metadata


@app.get('/api/v1/random_profile/last_name')
async def get_last_name(params: query_model = Depends()):
    """ Get multiple last names

    args:
        num (int): number of last names to generate

    """
    params_as_dict = params.dict()
    if params_as_dict['num'] > query_limit:
        return overloaded_error

    num = params_as_dict['num']
    last_names = rp.last_name(num)
    metadata['data'] = last_names
    return metadata


@app.get('/api/v1/random_profile/full_name')
async def get_full_name(params: query_model = Depends()):
    """ Get multiple full names

    args:
        num (int): number of full names to generate

    """
    params_as_dict = params.dict()
    if params_as_dict['num'] > query_limit:
        return overloaded_error

    num = params_as_dict['num']
    full_names = rp.full_name(num)
    metadata['data'] = full_names
    return metadata


@app.get('/api/v1/random_profile/ip_address')
async def get_ip_address(params: query_model = Depends()):
    """ Get multiple ip addresses

    args:
        num (int): number of ip addresses to generate

    """
    params_as_dict = params.dict()
    if params_as_dict['num'] > query_limit:
        return overloaded_error

    num = params_as_dict['num']
    ip_addresses = rp.ipaddress(num)
    metadata['data'] = ip_addresses
    return metadata


@app.get("/api/v1/random_profile/job_title")
async def get_job_title(params: query_model = Depends()):
    """ Get multiple job titles

    args:
        num (int): number of job titles to generate

    """
    params_as_dict = params.dict()
    if params_as_dict['num'] > query_limit:
        return overloaded_error

    num = params_as_dict['num']
    job_titles = rp.job_title(num)
    metadata['data'] = job_titles
    return metadata


@app.get("/api/v1/random_profile/address")
async def get_address(params: query_model = Depends()):
    """ Get multiple address """
    params_as_dict = params.dict()
    if params_as_dict['num'] > query_limit:
        return overloaded_error
    num = params_as_dict['num']
    address = rp.generate_address(num)
    metadata['data'] = address
    return metadata


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Random Profile Generator API",
        version=VERSION,
        description="Python Module To Generate Random Profile Data",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://raw.githubusercontent.com/DrakeEntity/project-Image/master/9b2ca712-347a-4987-bac7-a4c3d106ed24_200x200.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


def start_server(port=8000):
    uvicorn.run(app, host="0.0.0.0", port=port)
