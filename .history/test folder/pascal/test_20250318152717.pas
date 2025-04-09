program Factorial;
var
  n, i, fact: integer;
begin
  fact := 1;
  write('Enter a number: ');
  readln(n);
  for i := 1 to n do
    fact := fact * i;
  writeln('Factorial: ', fact);
end.
