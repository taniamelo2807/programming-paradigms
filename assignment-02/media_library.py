from abc import ABC, abstractmethod


MEDIA_DATA = [
    {"type": "song", "title": "Bohemian Rhapsody", "creator": "Queen", "duration": 354, "genre": "Rock"},
    {"type": "song", "title": "Blinding Lights", "creator": "The Weeknd", "duration": 200, "genre": "Pop"},
    {"type": "podcast", "title": "Lex Fridman #400", "creator": "Lex Fridman", "duration": 7200, "episode_number": 400},
    {"type": "audiobook", "title": "Clean Code", "creator": "Robert Martin", "duration": 25200, "chapters": 17},
]


class MediaItem(ABC):
    def __init__(self, title, creator, duration):
        if not title:
            raise ValueError("Title cannot be empty")

        if not creator:
            raise ValueError("Creator cannot be empty")

        if duration <= 0:
            raise ValueError("Duration must be greater than 0")

        self._title = title
        self._creator = creator
        self._duration = duration

    @property
    def title(self):
        return self._title

    @property
    def creator(self):
        return self._creator

    @property
    def duration(self):
        return self._duration

    @abstractmethod
    def describe(self):
        pass


class Song(MediaItem):
    def __init__(self, title, creator, duration, genre):
        super().__init__(title, creator, duration)
        self._genre = genre

    @property
    def genre(self):
        return self._genre

    def describe(self):
        return f"Song: {self.title} by {self.creator} [{self.genre}] ({self.duration}s)"


class Podcast(MediaItem):
    def __init__(self, title, creator, duration, episode_number):
        super().__init__(title, creator, duration)
        self._episode_number = episode_number

    @property
    def episode_number(self):
        return self._episode_number

    def describe(self):
        return f"Podcast: {self.title} by {self.creator} - episode {self.episode_number} ({self.duration}s)"


class Audiobook(MediaItem):
    def __init__(self, title, creator, duration, chapters):
        super().__init__(title, creator, duration)
        self._chapters = chapters

    @property
    def chapters(self):
        return self._chapters

    def describe(self):
        return f"Audiobook: {self.title} by {self.creator} - {self.chapters} chapters ({self.duration}s)"


class Playlist:
    def __init__(self, name, event_bus=None):
        self._name = name
        self._items = []
        self._event_bus = event_bus
        self._sort_strategy = SortByTitle()

    @property
    def name(self):
        return self._name

    def add_item(self, item):
        if not isinstance(item, MediaItem):
            raise TypeError("Playlist only accepts MediaItem objects")

        self._items.append(item)

        if self._event_bus is not None:
            self._event_bus.publish("item_added", {"title": item.title})

    def total_duration(self):
        return sum(item.duration for item in self._items)

    def set_sort_strategy(self, strategy):
        self._sort_strategy = strategy

    def items_sorted(self):
        return self._sort_strategy.sort(self._items)

    def __len__(self):
        return len(self._items)


class Library:
    def __init__(self, name):
        self._name = name
        self._playlists = {}

    def add_playlist(self, playlist):
        if not isinstance(playlist, Playlist):
            raise TypeError("Library only accepts Playlist objects")

        self._playlists[playlist.name] = playlist

    def statistics(self):
        total_items = 0
        total_duration = 0

        for playlist in self._playlists.values():
            total_items += len(playlist)
            total_duration += playlist.total_duration()

        return {
            "total_items": total_items,
            "total_duration": total_duration
        }


class EventBus:
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event, callback):
        if event not in self._subscribers:
            self._subscribers[event] = []

        self._subscribers[event].append(callback)

    def publish(self, event, payload):
        for callback in self._subscribers.get(event, []):
            callback(payload)


class SortByTitle:
    def sort(self, items):
        return sorted(items, key=lambda item: item.title.lower())


class SortByDuration:
    def sort(self, items):
        return sorted(items, key=lambda item: item.duration)


class CatalogExporter:
    def export(self, rows):
        return self.format_header() + self.format_rows(rows)

    def format_header(self):
        raise NotImplementedError

    def format_rows(self, rows):
        raise NotImplementedError


class CsvCatalogExporter(CatalogExporter):
    def format_header(self):
        return "type,title,duration\n"

    def format_rows(self, rows):
        lines = []

        for row in rows:
            line = f"{row['type']},{row['title']},{row['duration']}"
            lines.append(line)

        return "\n".join(lines)


def load_items(data):
    items = []

    for record in data:
        media_type = record["type"]

        if media_type == "song":
            item = Song(
                record["title"],
                record["creator"],
                record["duration"],
                record["genre"]
            )

        elif media_type == "podcast":
            item = Podcast(
                record["title"],
                record["creator"],
                record["duration"],
                record["episode_number"]
            )

        elif media_type == "audiobook":
            item = Audiobook(
                record["title"],
                record["creator"],
                record["duration"],
                record["chapters"]
            )

        else:
            raise ValueError(f"Unknown media type: {media_type}")

        items.append(item)

    return items


def run_media_hub():
    items = load_items(MEDIA_DATA)

    event_bus = EventBus()
    log = []

    event_bus.subscribe("item_added", lambda p: log.append(f"added:{p['title']}"))

    library = Library("My Media Library")
    playlist = Playlist("Main Playlist", event_bus)

    for item in items:
        print(item.describe())
        playlist.add_item(item)

    library.add_playlist(playlist)

    print(library.statistics())
    print(log)

    playlist.set_sort_strategy(SortByTitle())
    sorted_items = playlist.items_sorted()
    sorted_titles = [item.title for item in sorted_items]

    print("Sorted: " + " | ".join(sorted_titles))

    rows = []

    for item in items:
        rows.append({
            "type": type(item).__name__,
            "title": item.title,
            "duration": item.duration
        })

    exporter = CsvCatalogExporter()
    print(exporter.export(rows))


if __name__ == "__main__":
    run_media_hub()
