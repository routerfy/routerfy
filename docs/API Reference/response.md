# `Response` class

You can use it directly to create an instance of it and return it from your path operations.

You can import it directly from routerfy:

```python
from routerfy import Response
```

## **`class`** routerfy.Response

```python
Response(
    content=None,
    status_code=200,
    headers=None,
    media_type=None,
)
```


### **Example**

```python
from routerfy import APIRouter, Response

router = APIRouter("/users")

@router.get("/{user_id}")
def read_users(user_id):
    if user_id is None:
        return Response("not authorized", status_code=403)
    ...
    return {"message": "user found"}

```

| **PARAMETER** | **TYPE**                      | **DEFAULT**   |
| : ----------- | : --------------------------- | : ----------- |
| `content`     | `Any`                         | `None`        |
| `status_code` | `int`                         | `200`         |
| `headers`     | `Optional[Mapping[str, str]]` | `None`        |
| `media_type`  | `Optional[str]`               | `None`        |