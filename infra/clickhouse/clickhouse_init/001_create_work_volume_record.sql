CREATE TABLE IF NOT EXISTS default.work_volume_record
(
    factory UUID,
    start Date,
    finish Date,
    weight Int32,
    author Int64,
    created DateTime
)
ENGINE = MergeTree()
ORDER BY (factory, start);