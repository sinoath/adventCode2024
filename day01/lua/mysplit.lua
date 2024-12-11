local M = {}
local sentence = "this is   a  sentence with spaces"
function M.mysplit(phrase, pattern)
	local result = {}
	local start
	local beg, fin = string.find(phrase, pattern, 1)
	if beg == nil then
		return result
	end
	if beg > 1 then
		table.insert(result, string.sub(phrase, 1, beg - 1))
		start = fin + 1
	else
		start = fin + 1
	end
	repeat
		beg, fin = string.find(phrase, pattern, start)
		table.insert(result, string.sub(phrase, start, beg - 1))
		start = fin + 1
	until fin == string.len(phrase) or fin == nil
	return result
end

local test = M.mysplit(sentence, " ")

return M
