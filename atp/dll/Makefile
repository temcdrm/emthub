# File: makefile
# Purpose: compile and link atp
#
CC       = gcc.exe
FOR      = g77.exe

OBJECTS =analyt.o \
	comtac.o \
	devt69.o \
	dimdef.o \
	fgnmod.o \
	hopcod.o \
	newmods.o \
	user10.o \
	usernl.o \
	usrfun.o \
	usedll.o

INSFILE	= blkcom.ins \
	comta1.ins \
	comta2.ins \
	comta3.ins \
	deksal.ins \
	dekspy.ins \
	sixty4.ins \
	space2.ins \
	tacsar.ins

DLL_OBJS =dllfunc.o sample.o

DLL_NAME    = c:/atp/atpmingw/Dllfunc.dll

CFLAGS =  -DUNDERSCORE -O2
FFLAGS = -O2
IMAGE=c:/atp/atpmingw/mytpbig.exe

LIBRARY = c:/atp/atpmingw/make/tpbig.a c:/atp/atpmingw/make/dismg7.a \
          -Lc:/atp/atpmingw/make/MinGW/lib -lgdi32

all:	$(DLL_NAME) $(IMAGE)

.f.o:
	$(FOR) -c $(FFLAGS) $<
.c.o:
	$(CC) -c $(CFLAGS) $<

$(IMAGE) : $(OBJECTS) $(INSFILE)
	copy c:\atp\atpmingw\make\MinGW\lib\crt2.o > null
	$(FOR) -s -o $(IMAGE) $(OBJECTS) $(LIBRARY)
	del crt2.o > null

dllfunc.o: dllfunc.c
	$(CC) -c $(CFLAGS) dllfunc.c

usedll.o: usedll.c
	$(CC) -c $(CFLAGS) usedll.c

sample.o: sample.f
	$(FOR) -c $(FFLAGS) sample.f

$(DLL_NAME): $(DLL_OBJS)
	$(CC) -shared -o $(DLL_NAME) $(DLL_OBJS) \
		-Wl,--export-all-symbols

clean:
	del *.o
#	del $(DLL_NAME)
#	del $(IMAGE)
