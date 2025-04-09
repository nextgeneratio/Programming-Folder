program Fibonacci;
var
  n, i, a, b, c: integer;
begin
  write('Enter number of terms: ');
  readln(n);
  a := 0;
  b := 1;
  writeln(a);
  writeln(b);
  for i := 3 to n do
  begin
    c := a + b;
    writeln(c);
    a := b;
    b := c;
  end;
end.
