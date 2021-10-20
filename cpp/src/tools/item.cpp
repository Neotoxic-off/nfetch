#include <tools.hpp>

Item Tools::get_item(char *line)
{
    Item item;
    std::string converted(line);
    item.key = converted.substr(0, converted.find("="));
    item.value = converted.erase(0, converted.find("=") + 1);

    return (item);
}
