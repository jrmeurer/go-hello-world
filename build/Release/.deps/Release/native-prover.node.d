cmd_Release/native-prover.node := c++ -bundle -undefined dynamic_lookup -Wl,-no_pie -Wl,-search_paths_first -mmacosx-version-min=10.10 -arch x86_64 -L./Release -stdlib=libc++  -o Release/native-prover.node Release/obj.target/native-prover/native-prover-addon.o ../lib/native-prover.a