KDIR ?= "/lib/modules/`uname -r`/build"
PWD := $(CURDIR)

obj-m += main.o

all:
	$(MAKE) -C $(KDIR) M=$(PWD) modules

clean:
	$(MAKE) -C $(KDIR) M=$(PWD) clean
