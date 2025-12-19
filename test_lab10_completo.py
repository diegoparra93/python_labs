import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'src'))

print("=== TEST COMPLETO LAB 10 ===")

try:
    from lab10 import Stack, Queue, SinglyLinkedList
    print("✅ Todos los módulos importados correctamente")
    
    print("\n1. 🔹 STACK (LIFO):")
    s = Stack()
    s.push("A")
    s.push("B")
    s.push("C")
    print(f"   Stack: {s}")
    print(f"   Pop: {s.pop()}")
    print(f"   Peek: {s.peek()}")
    print(f"   Tamaño: {len(s)}")
    
    print("\n2. 🔹 QUEUE (FIFO):")
    q = Queue()
    q.enqueue("Primero")
    q.enqueue("Segundo")
    q.enqueue("Tercero")
    print(f"   Queue: {q}")
    print(f"   Dequeue: {q.dequeue()}")
    print(f"   Queue después: {q}")
    
    print("\n3. 🔹 LINKED LIST:")
    ll = SinglyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.prepend(5)
    ll.insert(2, 15)
    print(f"   Lista: {ll}")
    print(f"   Display: {ll.display()}")
    print(f"   Tamaño: {len(ll)}")
    
    print("\n   Iteración:")
    for item in ll:
        print(f"     - {item}")
    
    ll.remove(15)
    print(f"\n   Después de remove(15): {ll}")
    
    print("\n" + "="*50)
    print("🎉 ¡LAB 10 COMPLETADO EXITOSAMENTE!")
    print("="*50)
    
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
