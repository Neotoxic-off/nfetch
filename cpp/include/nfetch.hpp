#ifndef NFETCH_HPP
    #define NFETCH_HPP

    // Standard libraries
    #include <required.hpp>
    
    // Macros & defines
    #include <macro.hpp>

    // Structures
    #include <item.hpp>

    // Classes
    #include <tools.hpp>

    class Nfetch
    {
        public:
            Nfetch(char **);
            ~Nfetch();

            bool loader(char **);

            // check
            bool update(Item);
            bool display();

        private:
            // Classes
            Tools tools;

            // Variables
            std::map<std::string, std::string> status = {
                { "GDMSESSION", EMPTY },
                { "SHELL", EMPTY },
                { "USER", EMPTY }
            };
            std::map<std::string, std::string> alias = {
                { "GDMSESSION", "WM" },
                { "SHELL", "Shell" }
            };
    };

#endif // !NFETCH_HPP

