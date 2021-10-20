#include <nfetch.hpp>

Nfetch::Nfetch(char **env)
{
    this->loader(env);

    return;
}

Nfetch::~Nfetch()
{
    return;
}

bool Nfetch::loader(char **env)
{
    for (std::size_t i = 0; env[i] != NULL; i++) { 
        this->update(
            this->tools.get_item(env[i])
        );
    }

    Nfetch::display();

    return (false);
}

bool Nfetch::update(Item item)
{
    if (this->status.find(item.key) != this->status.end()) {
        this->status[item.key] = item.value;
    }

    return (false);
}

bool Nfetch::display()
{
    for (auto i = this->status.begin(); i != this->status.end(); i++) {
        std::cout << this->alias[i->first] << " : " << i->second << std::endl;
    }

    return (false);
}
