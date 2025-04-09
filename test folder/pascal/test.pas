program MaxNumber;
var
  a, b, c: integer;
begin
  write('Enter three numbers: ');
  readln(a, b, c);
  if (a >= b) and (a >= c) then
    writeln('Maximum: ', a)
  else if (b >= a) and (b >= c) then
    writeln('Maximum: ', b)
  else
    writeln('Maximum: ', c);
end.
