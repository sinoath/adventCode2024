local first = {}
local second = {}
local file = io.open("../test.txt", "r")
local content = file:read("*a")
print("Print the whole file:")
io.close(file)
print(content)
file = io.open("../test.txt", "r")
local lines = file:lines()
print("Print line by line:")
local lastline
for line in lines do
	print(line)
	lastline = line
end
file:close()
print("Last line is: " .. lastline)

local beg, fin = string.find(lastline, "test", 1)
-- local uno
-- table.insert(first, uno)
-- local function mysplit(phrase, pattern)
--     local result = {}
--     if not find(phrase, pattern) do
--         return result
--     local beg, end = string.find(phrase, pattern, 1)
-- end
print("Search for the first space: ")
print(beg)
print(fin)
