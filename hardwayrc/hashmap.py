def new(num_buckets=256):
    """Initializes a Map with the given number of buckets."""
    # hokay. so. this function makes a hashmap, and is also known as an
    # initializer.
    # create aMap variable, a list
    aMap = []
    for i in range(0, num_buckets):
        # put num_buckets in our aMap list
        aMap.append([])
        return aMap
        # they're gonna hold the contents of the hashmaps. neat!
        # later we'll use len(aMap) to discover the number of buckets

def hash_key(aMap, key):
    """
    Given a key, this will create a number and then convert it to an index
    for the aMap's buckets.
    """
    # the core of how a dict works. uses built-in hash function to convert a
    # string into a number. wacky! and awesome.
    # Python uses this function for its own dict data structure, so it's good
    # enough for us.
    # use our bud the modulus operator to get a bucket where the key goes
    # this has the effect of limiting a humongous number to a fixed lil set.
    # it is also cool as heck.
    return hash(key) % len(aMap)

def get_bucket(aMap, key):
    """Given a key, find the bucket where it would go."""
    # uses hash_key to find a bucket that *might* contain a key.
    # the % len(aMap) in hash_key ensures whatever bucket_id we get will fit
    # into the aMap list, so we can use that (the bucket_id) to figure out
    # where the key could feasibly be located.
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id]

def get_slot(aMap, key, default=None):
    """
    Returns the index, key, and value of a slot found in a bucket.
    Returns -1, key, and default (None if not set) when not found.
    """
    # find out what bucket a key could be in
    bucket = get_bucket(aMap, key)

    # roll through every element of the bucket, checking for a matching key
    for i, kv in enumerate(bucket):
        k, v = kv
        # hot diggity; found the key
        if key == k:
            # returns this lil tuple which is the index the key was found in,
            # the key itself, and the value set for that key
            return i, k, v

    return -1, key, default

def get(aMap, key, default=None):
    """Gets the value in a bucket for the given key, or the default."""
    # "convenience function" which uses get_slot to get i, k, v, and then just
    # return the v (too bad for i and k).
    i, k, v = get_slot(aMap, key, default=default)
    return v

def set(aMap, key, value):
    """Sets the key to the value, replacing any existing value."""
    # slower here, but faster on get (could also implement the other way)
    # fetch the bucket
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key)

    # does this key already exist? we're not allowing more than one value
    # for a key.
    if i >= 0:
        # the key exists; replace it
        bucket[i] = (key, value)
    else:
        # the key does not; append to create it
        # overall this strategy is slower than just appending, but more likely
        # what a user of hashmap wants
        bucket.append((key, value))

def delete(aMap, key):
    """Deletes the given key from the Map."""
    # find the bucket! my favorite bucket-related game
    bucket = get_bucket(aMap, key)

    # look for the key in the bucket
    for i in xrange(len(bucket)):
        k, v = bucket[i]
        if key == k:
            # and if it's found, delete it
            del bucket[i]
            # we can stop there, because we disallowed duplicates
            break

def list(aMap):
    """Prints out what's in the Map."""
    # wee lil debug function. prints out what's in the hashmap.
    # fetch each bucket
    for bucket in aMap:
        if bucket:
            # goes through each slot in the bucket
            for k, v in bucket:
                print k, v

# There is an interesting study drill:
# 4. Read about Python’s assert feature and then take the hashmap code and add
# assertions for each of the tests I’ve done instead of print. For example, you
# can assert that the first get operation returns ”Flamenco Sketches” instead
# of just printing that out.

# That sounds good and fine, but I can't figure out what tests he's talking
# about. Eerily similar to "After all of these functions I just have a little
# bit of testing code that makes sure they work," which also confounded me. Dang.
# I cannot figure out what the testing code is. I don't actually think it's the
# ex39_test.py code, although that would be convenient.
