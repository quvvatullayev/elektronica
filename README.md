# elektronica Documentation

## base url : `http://elektronica.pythonanywhere.com/`

# database schema

<!-- ![alt text](kun_uz_img.png) -->

## `eliments api`

| Method | path | description |
| --- | --- | --- |
| GET | `/eliments` | get all eliments |

### Response

| key | type | description |
| --- | --- | --- |
| id | int | id of eliment |
| key | string | key of eliment |
| description | string | description of eliment |

```python
{
    "id": int,
    "key": string,
    "description": string
}
```


## `eliment info api`

| Method | path | description |
| --- | --- | --- |
| GET | `/eliment_info/<int:eliment_id>` | get eliment info |
| GET | `/eliment_info/` | get all eliment info |ElimentsCount


### Response

| key | type | description |
| --- | --- | --- |
| id | int | id of eliment info |
| key | string | key of eliment info |
| description | string | description of eliment info |
| value | string | value of eliment info |
| formula | img | formula of eliment info |
| eliment | int | id of eliment |


```python
{
    "id": int,
    "key": string,
    "description": string,
    "value": string,
    "formula": img,
    "eliment_id": int
}
```

## `Eliments Count api`

| Method | path | description |
| --- | --- | --- |
| GET | `/eliments_count/<int:pk>` | get eliment count |

### Request

| key | type | description |
| --- | --- | --- |
| pk | int | id of eliment |
 
### Request body
    
```python
{
    "key":int
}
```

### Response

| key | type | description |
| --- | --- | --- |
| result | int | count of eliment |

```python
{
    "result": int
}
```
or 

```python
{
    "result": "NameError"
}
```