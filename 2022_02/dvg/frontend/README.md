# frontend

## How this was created

```
nvm install --lts
npx @vue/cli create frontend --default
npx @vue/cli add router
npx @vue/cli add apollo
```

## Project setup
```
npm install bootstrap@4.6.0 bootstrap-vue@2.21.2

```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Sample Graph Queries 

```
{
  allPosts {
    title
    subtitle
    author {
      user {
        username
      }
    }
    tags {
      name
    }
  }
}
```

### Issues in hosting

`unset HOST`
