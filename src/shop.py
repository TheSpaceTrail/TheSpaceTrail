from . import terminal

import rich.align
import rich.text
import rich.live

class Item:

    def __init__(self, name, emoji, price, id="pass"):

        self.name = name
        self.emoji = emoji
        self.price = int(price)
        self.selected = False
        self.id = id

class shop:

    def __init__(self, 
        tstt: terminal.terminal, 

        title: str,

        store_keeper_name: str,
        store_keeper_msg: str,
        player: dict
    ):

        self.tstt = tstt

        self.title = title

        self.store_keeper_name = store_keeper_name
        self.store_keeper_msg = store_keeper_msg

        self.changed = False
        self.player = player

        self.items: list[Item] = []
        self.diff = 0

    def add_items(self, items: list):

        self.items.extend(items)

    def render(self):

        items_rendered = ""

        self.credits = self.player["credits"]

        idx = 1

        for item in self.items:

            item_render = f"{idx}. {item.emoji} {item.name} {item.price}"

            style = "white"

            if item.price < self.credits:

                style = "bright_black"

            elif item.price > self.credits:

                style = "dark_red"
            
            elif item.name == "Exit":

                style = "green"
            
            items_rendered += f"\n[{style}]{item_render}[/{style}]"
            
            idx += 1

        diff = self.diff
        self.diff = 0

        diff_text = ""

        if diff > 0:
            diff_text = f"[red](-{diff})[/red]"

        rendered = f"{self.title}" \
            + "\n--------" \
            + f"\n{self.store_keeper_name}: {self.store_keeper_msg}" \
            + f"\nSpace Yen: {self.credits} {diff_text}" \
            + f"\n--------\n" \
            + f"\n{items_rendered}" \
            + f"\n[green]x. Exit[/green]"

        self.changed = True
        
        return rendered
    
    def run(self):

        with rich.live.Live(console=self.tstt.console, refresh_per_second=60) as live:

            while True:

                rendered = ""

                rendered = self.render()

                display = rich.text.Text()

                for segment in rich.text.Text.from_markup(rendered).render(self.tstt.console):

                    display.append(segment.text, style=segment.style)

                
                if self.changed:
                    live.update(rich.align.Align(rendered, align="center"))
                    self.changed = False
                
                live.stop()
                
                prompt_value = input("Which item would you like to buy? > ")
                try: item_idx = int(prompt_value)-1
                except: 
                    if prompt_value.lower() == "x" or prompt_value.lower() == "exit": return ""
                    continue

                self.tstt.clear_screen()

                live.start()

                try:
                    item_chosen = self.items[item_idx]
                except:
                    pass # They should know that their selection is wrong from the highlighting
                    
                self.tstt.clear_screen()

                live.update(rich.align.Align(rendered, align="center"))

                number_of_items = 1

                if not item_chosen.price > self.credits:
                    
                    live.stop()
                    number_of_items = int(input("How many would you like to buy? > "))

                    if number_of_items <= 0:
                        self.store_keeper_msg = "Sorry?"
                        continue

                    self.tstt.clear_screen()
                    live.start()

                if item_chosen.price*number_of_items > self.credits:

                    self.store_keeper_msg = "Insufficient funds!"
                
                else:

                    self.store_keeper_msg = f"You bought {number_of_items} {item_chosen.name}s!"

                    self.player[item_chosen.id] += number_of_items
                    self.player["credits"] -= item_chosen.price*number_of_items

                    self.diff = item_chosen.price*number_of_items

                    #print(self.player)


if __name__ == "__main__":

    shoppy= shop(terminal.terminal(rich.get_console()), 1000, "John's shop", "John", "Good afternoon!")
            
    shoppy.add_items([Item("Meat", "🍖", 5000)])

    shoppy.run()
            

        
