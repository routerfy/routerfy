[![License](https://img.shields.io/npm/l/tasker-man.svg)](https://github.pactual.net/bruno-s-junqueira/routerfy/blob/main/LICENSE)

Routerfy is an easy, fast and modern framework for building AWS Serverless applications with python 3.7+ using FastAPI for development and a lighter lambda layer on AWS Lambda execution.

---

**Documentation**: <a href="https://routerfy.github.io/" target="_blank">Docs</a>

**Source Code**: <a href="https://github.com/routerfy/routerfy/">GitHub</a>

---

Key features are:

* **Light**: Routerfy's lambda layer it's extremely light since it does not need any additional library to redirect routes.
* **Fast to test**: Increase the speed to test new features by about 500%.
* **Fast to build templates**: Building AWS templates never been that easy. Routerfy create all AWS templates with necessary properties but still customizable.
* **Familiar Syntax**: Routerfy use same syntax of FastAPI for routes creation turning the experience of migration a lot easier.
* **Body Validation**: Routerfy have an own route body validation like pydantic but lighter using no dependencies.


## Requirements

Python 3.7+

For development serving, Routerfy uses the amazing ones:

* [FastAPI](https://fastapi.tiangolo.com/) for route management.
* [Uvicorn](https://www.uvicorn.org/) for ASGI server.


## Installation

**For development:**
```bash
pip install routerfy[dev]
```
**For AWS Lambda layer:**
```bash
pip install routerfy
```

## Getting Started

To create your first Routerfy project you only need to use `create` command. Open CMD in the folder you want to create your project and insert:
```bash
routerfy create MyAwesomeRouterfyProject
```

If everything go well the project folder created will look like this: 

```md
.
├─ routes/
│  ├─ hello_world/
│  │  ├─ app.py
│  │  ├─ route.py
└─ routerfy.config.yaml
```

### Example

Our first example file is the `route.py` inside the lambda folder `hello_world`. All lambda folders must have a `route.py`. this way routerfy can identify routers and make the magic happens.

```python
from routerfy import APIRouter, Response

router = APIRouter(prefix="/hello")

@router.get("/")
def hello_world_get_request():
    return "Hello World!"
```

As you can see, the syntax is very similar to FastAPI.

### Testing application

To test application you only need to use the `dev` command on your project terminal:
```bash
routerfy dev
```

The server will start and you will have your routerfy application served locally!
