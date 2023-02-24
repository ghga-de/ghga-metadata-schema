```mermaid
erDiagram
Submission {

}
Dataset {

}
File {

}

Submission ||--}| File : "has file"
Submission ||--}| Dataset : "has dataset"
Dataset ||--}| File : "has file"

```

