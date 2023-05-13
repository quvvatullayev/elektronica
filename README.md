# elektronica Documentation

## `eliments api`

| Method | path | description |
| --- | --- | --- |
| GET | `/eliments` | get all eliments |

### `Response`

| key | type | description |
| --- | --- | --- |
| id | int | id of eliment |
| key | string | key of eliment |
| description | string | description of eliment |

```json
{
    "id": int,
    "key": string,
    "description": string
}
```


## `eliment info api`

| Method | path | description |
| --- | --- | --- |
| GET | `/eliment_info/<eliment_id>` | get eliment info |
| GET | `/eliment_info/` | get all eliment info |

### `Response`

| key | type | description |
| --- | --- | --- |
| id | int | id of eliment info |
| key | string | key of eliment info |
| description | string | description of eliment info |
| value | string | value of eliment info |
| formula | img | formula of eliment info |
| eliment | int | id of eliment |


```json
{
    "id": int,
    "key": string,
    "description": string,
    "value": string,
    "formula": img,
    "eliment_id": int
}
```