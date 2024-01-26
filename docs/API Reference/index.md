# `APIRouter` class

Here's the reference information for the routerfy `APIRouter` class, with all its parameters, attributes and methods.

You can import the `APIRouter` class directly from `routerfy`:
```python
from routerfy import APIRouter
```

## **`class`** routerfy.APIRouter

```python
APIRouter(
    *,
    prefix="",
)
```

`APIRouter` class used to group path operations, for example to structure an app in multiple files.

### **Example**

```python
from routerfy import APIRouter

router = APIRouter("/users")

@router.get("/")
def read_users():
    return [{"username": "XG4mer"}, {"username": "MrJunkes"}]

```

| **PARAMETER** | **DESCRIPTION**                                                               | **TYPE** | **DEFAULT** |
| : ----------- | : --------------------------------------------------------------------------- | : ------ | : --------- |
| `prefix`      | An optional path prefix for the router used to define methods prefixed paths. | `str`    | `''`        |

### **`method`** get()

```python
get(
    path
)
```

Add a *path operation* using an HTTP GET operation.

#### **Example**

```python
from routerfy import APIRouter

router = APIRouter()

@router.get("/items")
def read_items():
    return [{"name": "Rope"}, {"name": "Tire"}]

```

| **PARAMETER** | **DESCRIPTION**                                                               | **TYPE** |
| : ----------- | : --------------------------------------------------------------------------- | : ------ |
| `path`      | The URL path to be used for this path operation. For example, in `https://example.com/items`, the path is `/items`. | `str`    |

### **`method`** post()

```python
post(
    path
)
```

Add a *path operation* using an HTTP POST operation.

#### **Example**

```python
from routerfy import APIRouter, BaseModel

router = APIRouter()

class Item(BaseModel):
    name: str
    description: str | None = None

@router.post("/items")
def post_item(item: Item):
    return {"message": "Item created successfully!"}

```

| **PARAMETER** | **DESCRIPTION**                                                               | **TYPE** |
| : ----------- | : --------------------------------------------------------------------------- | : ------ |
| `path`      | The URL path to be used for this path operation. For example, in `https://example.com/items`, the path is `/items`. | `str`    |

### **`method`** put()

```python
put(
    path
)
```

Add a *path operation* using an HTTP PUT operation.

#### **Example**

```python
from routerfy import APIRouter, BaseModel

router = APIRouter()

class Item(BaseModel):
    name: str
    description: str | None = None

@router.put("/items/{item_id}")
def update_item(item: Item, item_id):
    return {"message": "Item updated!"}

```

| **PARAMETER** | **DESCRIPTION**                                                               | **TYPE** |
| : ----------- | : --------------------------------------------------------------------------- | : ------ |
| `path`      | The URL path to be used for this path operation. For example, in `https://example.com/items`, the path is `/items`. | `str`    |

### **`method`** patch()

```python
patch(
    path
)
```

Add a *path operation* using an HTTP PATCH operation.

#### **Example**

```python
from routerfy import APIRouter, BaseModel

router = APIRouter()

class Item(BaseModel):
    name: str
    description: str | None = None

@router.patch("/items/")
def update_item(item: Item):
    return {"message": "Item updated in place"}

```

| **PARAMETER** | **DESCRIPTION**                                                               | **TYPE** |
| : ----------- | : --------------------------------------------------------------------------- | : ------ |
| `path`      | The URL path to be used for this path operation. For example, in `https://example.com/items`, the path is `/items`. | `str`    |

### **`method`** delete()

```python
delete(
    path
)
```

Add a *path operation* using an HTTP DELETE operation.

#### **Example**

```python
from routerfy import APIRouter

router = APIRouter()

@router.delete("/items/{item_id}")
def delete_item(item_id):
    return {"message": "Item deleted!"}

```

| **PARAMETER** | **DESCRIPTION**                                                               | **TYPE** |
| : ----------- | : --------------------------------------------------------------------------- | : ------ |
| `path`      | The URL path to be used for this path operation. For example, in `https://example.com/items`, the path is `/items`. | `str`    |

### **`method`** options()

```python
options(
    path
)
```

Add a *path operation* using an HTTP OPTIONS operation.

#### **Example**

```python
from routerfy import APIRouter

router = APIRouter()

@router.options("/items")
def get_item_options():
    return {"additions": ["Chair", "Broom"]}

```

| **PARAMETER** | **DESCRIPTION**                                                               | **TYPE** |
| : ----------- | : --------------------------------------------------------------------------- | : ------ |
| `path`      | The URL path to be used for this path operation. For example, in `https://example.com/items`, the path is `/items`. | `str`    |