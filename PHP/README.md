<div style="text-align: center">
    <h1>PHP</h1>
</div>

<details>
    <summary>debug backtrace - Выводит стек вызовов функций в массив </summary>

`debug_backtrace()` - Выводит стек вызовов функций в массив  

```php
file_put_contents(__DIR__ . '/trace.txt', (new Exception())->getTraceAsString(), FILE_APPEND);
echo debug_print_backtrace(DEBUG_BACKTRACE_IGNORE_ARGS);
```

</details>

